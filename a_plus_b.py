# y = a^2 * x + b 를 계산하는 함수
def compute_y(a, x, b):
    return (a ** 2) * x + b


def main():
    print("=== y = a^2 * x + b 계산 프로그램 ===")

    # 1) a, b, X의 최대값 입력 받기
    a = int(input("a: "))
    b = int(input("b: "))
    max_x = int(input("Max: "))

    # 2) X를 0부터 max_x까지 증가시키면서 y 출력
    for x in range(0, max_x + 1):   # 0 ~ max_x 포함
        y = compute_y(a, x, b)
        # 예시: 2x2x0 + 1 = 1
        print(f"{a}x{a}x{x} + {b} = {y}")


# 이 파일을 직접 실행했을 때만 main()이 실행되도록
if __name__ == "__main__":
    main()