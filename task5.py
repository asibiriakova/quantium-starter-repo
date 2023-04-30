from task4 import app


def test_elements_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h1").text == "Sales in Regions by Date"
    assert dash_duo.find_element("#graph") is not None
    assert dash_duo.find_element("#region-picker") is not None