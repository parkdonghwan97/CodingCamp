def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    mid_peg = 6 - start_peg - end_peg  # mid_peg는 다음과 같이 정의됩니다. 세 개의 기둥 값의 합은 언제나 6이기 때문에

    if num_disks == 0:           #
        return None
    else:

        if num_disks == 1:  # base case

            move_disk(num_disks, start_peg, end_peg)

        elif num_disks == 2:

            hanoi(num_disks - 1, start_peg, mid_peg)
            move_disk(num_disks, start_peg, end_peg)
            hanoi(num_disks - 1, mid_peg, end_peg)

        else:

            hanoi(num_disks - 1, start_peg, mid_peg)
            move_disk(num_disks, start_peg, end_peg)
            hanoi(num_disks - 1, mid_peg, end_peg)


hanoi(3, 1, 3)