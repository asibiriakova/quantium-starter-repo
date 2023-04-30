from task4 import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)


def test_graph_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#graph", timeout=10)


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-picker", timeout=10)