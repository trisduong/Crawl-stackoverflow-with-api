def get_question(input_N, input_label):
    result = []
    import requests
    url = "https://api.stackexchange.com/questions?sort=votes&tagged={}&site=stackoverflow".format(
        input_label
    )
    ses = requests.Session()
    resp = ses.get(url, timeout=5)
    data = resp.json()
    for item in data['items']:
        result.append([item['title'], item['link']])
    page = 1
    while page * 30 < int(input_N):
        page += 1
        resp = ses.get(url, timeout=5, params={'page': page})
        for item in data['items']:
            result.append([item['title'], item['link']])
    return result


def main():
    import sys

    N, label = sys.argv[1], sys.argv[2]
    print(get_question(N, label)[0])


if __name__ == "__main__":
    main()
