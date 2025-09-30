import dad


def test_smoke():
    model = dad.load_DaD()
    assert model is not None