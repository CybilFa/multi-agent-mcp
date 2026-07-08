import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class MCPClient:
    """
    Reusable MCP Client for communicating with the MCP Server.
    """

    def __init__(self):

        self.server_params = StdioServerParameters(
            command="python",
            args=["-m", "mcp_server.server"],
        )

        self._stdio = None
        self._session = None

    async def connect(self):
        """
        Start the MCP connection and initialize the session.
        """

        self._stdio = stdio_client(self.server_params)

        read, write = await self._stdio.__aenter__()

        self._session = ClientSession(read, write)

        await self._session.__aenter__()

        await self._session.initialize()

        print("✅ MCP Client Connected")

    async def list_resources(self):
        """
        List all available MCP resources.
        """

        return await self._session.list_resources()

    async def list_tools(self):
        """
        List all available MCP tools.
        """

        return await self._session.list_tools()

    async def read_resource(self, uri: str):
        """
        Read an MCP resource.
        """

        return await self._session.read_resource(uri)

    async def summarize(self, text: str):
        """
        Call the summarize tool.
        """

        return await self._session.call_tool(
            "summarize",
            arguments={"text": text},
        )

    async def keywords(self, text: str):
        """
        Call the keywords tool.
        """

        return await self._session.call_tool(
            "keywords",
            arguments={"text": text},
        )

    async def close(self):
        """
        Close the MCP connection.
        """

        if self._session:
            await self._session.__aexit__(None, None, None)

        if self._stdio:
            await self._stdio.__aexit__(None, None, None)

        print("👋 MCP Client Closed")


async def test():

    client = MCPClient()

    await client.connect()

    tools = await client.list_tools()

    print("\nAvailable Tools")

    for tool in tools.tools:
        print("-", tool.name)

    summary = await client.summarize(
        "Artificial Intelligence is transforming modern software engineering."
    )

    print("\nSummary")

    print(summary)

    keywords = await client.keywords(
        "Artificial Intelligence is transforming modern software engineering."
    )

    print("\nKeywords")

    print(keywords)

    await client.close()


if __name__ == "__main__":
        asyncio.run(test())
