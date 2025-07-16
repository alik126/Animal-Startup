from app.batcher import split_batches


def test_split_batches():
    data = list(range(250))
    batches = split_batches(data, 100)
    assert len(batches) == 3
    assert len(batches[0]) == 100
    assert len(batches[2]) == 50
