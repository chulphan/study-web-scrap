from retrying import retry
import requests as req

TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)

def main():
    """
    메인처리
    """
    res = fetch('http://httpbin.org/status/200,404,503')
    if 200 <= res.status_code < 300:
        print('Success!')
    else:
        print('Error')

# stop_max_attempt_number: 최대 재시도 횟수
# wait_exponential_multiplier: 특정한 시간만큼 대기하고 재시도. 단위는 밀리초
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000)
def fetch(url):
    """
    지정한 URL에 요청한 뒤 Response 객체를 반환
    일시적인 오류가 발생하면 최대 3번 재시도.
    """
    print('Retrieving {0}...'.format(url))

    res = req.get(url)
    print('Status {0}...'.format(res.status_code))

    if res.status_code not in TEMPORARY_ERROR_CODES:
        #오류가 없다면 res 반환
        return res
    # 오류가 있다면 예외발생시킴.
    raise Exception('Temporary Error: {0}'.format(res.status_code))

if __name__ == '__main__':
    main()
