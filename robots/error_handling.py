import time
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

def fetch(url):
    """
    지정한 URL에 요청한 뒤 Response 객체를 반환
    일시적인 오류가 발생하면 최대 3번 재시도.
    """
    max_retries = 3 # 최대 3번 재시도.
    retries = 0 # 현재 재시도 횟수를 나타내는 변수
    while True:
        try:
            print('Retrieving {0}...'.format(url))
            res = req.get(url)
            print('Status: {0}'.format(res.status_code))
            if res.status_code not in TEMPORARY_ERROR_CODES:    
                return res # 일시적인 오류가 아니라면 res를 반환.
        except req.exceptions.RequestException as ex:
            # 네트워크 레벨 오류(RequestException)의 경우 재시도.
            print('Exception occured: {0}'.format(ex))

        retries += 1

        if retries >= max_retries:
            #재시도 횟수 상한을 넘으면 예외를 발생시킴.
            raise Exception('Too many retries...')
        wait = 2 ** (retries - 1)
        print('Waiting {0} seconds...'.format(wait))
        time.sleep(wait) # wait에 명시된 숫자만큼 대기

if __name__ == '__main__':
    main()
