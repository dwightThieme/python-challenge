def print_out(
    dividend,
    divisor,
    last_dividend_mult,
    last_divisor_mult,
    dividend_mult,
    divisor_mult,
    f_len=0,
    g_len=0,
):

    f_divs = "{0:{6},} {1:{6},}    {2:{6},}{3:{6},}  {4:{6},}{5:{6},}"
    arg_divs = [
        dividend,
        divisor,
        last_dividend_mult,
        last_divisor_mult,
        dividend_mult,
        divisor_mult,
        f_len,
    ]

    f_Euclid = "    {0:{4},} = {1:,}*({2:,}) + {3:,}"
    arg_Euclid = [dividend, dividend // divisor, divisor, dividend % divisor, f_len]

    print(f_divs.format(*arg_divs), f_Euclid.format(*arg_Euclid))
    print()


def print_gcd(m, n):
    coefficients = gcds(m, n)
    gcd = coefficients[0]
    m_c = coefficients[1]
    n_c = coefficients[2]
    f_Euclid = "{0:,}*({1:,}) + {2:,}*({3:,}) = {4:,}"
    print(f_Euclid.format(m_c, m, n_c, n, gcd))


def gcds(
    dividend,
    divisor,
    last_dividend_mult=1,
    last_divisor_mult=0,
    dividend_mult=0,
    divisor_mult=1,
    print_it=False,
    f_len=0,
    g_len=0,
    answer=None,
):

    if print_it:
        if not dividend_mult:
            f_len = max(len(str(dividend)), len(str(divisor)))
            f_len += f_len // 3
            g_len = len(
                str(
                    "{0:{4},} = {1:,}*({2:,}) + {3:,}".format(
                        dividend,
                        dividend // divisor,
                        divisor,
                        dividend % divisor,
                        f_len,
                    )
                )
            )

        print_out(
            dividend,
            divisor,
            last_dividend_mult,
            last_divisor_mult,
            dividend_mult,
            divisor_mult,
            f_len,
            g_len,
        )

    quotient = dividend // divisor
    remainder = dividend % divisor

    if remainder:
        return gcds(
            divisor,
            remainder,
            dividend_mult,
            divisor_mult,
            last_dividend_mult - dividend_mult * quotient,
            last_divisor_mult - divisor_mult * quotient,
            print_it,
            f_len,
            g_len,
        )

    else:
        if print_it:

            f_terminate = "{0:{4},} {1:{4},}{2:{5}} {3:_^{6}}"
            arg_terminate = [
                divisor,
                remainder,
                " ",
                "END OF EUCLIDEAN ALGORITHM",
                f_len,
                4 * f_len + 6,
                g_len + 5,
            ]

            print(f_terminate.format(*arg_terminate))
            print()

        answer = [divisor, dividend_mult, divisor_mult]
        return tuple(answer)


a = 902311
b = 3098766

an = gcds(a, b, print_it=True)
gcd = a * an[1] + b * an[2]


print_gcd(11134431, 777107)

arg_list = ["dividend", "divisor", "quotient", "remainder"]
print(*arg_list)

print_gcd(431, 77)
