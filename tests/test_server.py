from mcp_server.server import sample_document


def test_resource_exists():

    resource = sample_document()

    assert isinstance(resource, str)

    assert len(resource) > 0
    