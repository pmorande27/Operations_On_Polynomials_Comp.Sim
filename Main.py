from Polynomial import Polynomial


def main():
    a = Polynomial([1, 2, 3, 4, 5])
    b = Polynomial([2, 3, 4, 5, 6, 5, 65, 7, 8, 98])
    c = b.add_polynomials(a).coefficients
    print(a.integration().coefficients)
    a.toString()


main()
