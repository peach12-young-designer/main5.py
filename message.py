def simp():
    l = 0
    while l < 1:
        exam = 2
        while exam < p:
            if mod(p, exam) != 0:
                exam += 1
            else:
                break
        if exam == p:
            l += 1
    l = 0
    while l < 1:

        if q == p:
            break
        exam = 2
        while exam < q:
            if mod(q, exam) != 0:
                exam += 1
            else:
                break
        if exam == q:
            l += 1