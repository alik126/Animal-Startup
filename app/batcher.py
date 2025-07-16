def split_batches(data, batch_size):
    result = []
    for i in range(0, len(data), batch_size):
        result.append(data[i:i + batch_size])
    return result
