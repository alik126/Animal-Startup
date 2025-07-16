from app.transformer import transform_friends, transform_born_at


def test_transform_friends():
    assert transform_friends("Dog, Cat") == ["Dog", "Cat"]
    assert transform_friends("") == []
    assert transform_friends(None) == []


def test_transform_born_at():
    result = transform_born_at(716536042302)
    assert result.endswith("Z")
    assert "1992-09-15T05:47" in result
