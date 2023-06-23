def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    maleNum = int(input("How many male students are in the class? "))
    femaleNum = int(input("How many female students are in the class? "))

    total = maleNum + femaleNum
    m_perc = (maleNum / total) * 100
    f_perc = (femaleNum / total) * 100

    print(f"Total students: {total}")
    print(f"Number of males and females: {maleNum}\t{femaleNum}")
    print(f"The percentage of males and females: {m_perc:.2f}% \t{f_perc:.2f}%")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
