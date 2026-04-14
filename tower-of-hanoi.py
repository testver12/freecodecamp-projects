def hanoi_solver(n):
    ans = []
    top_rod = list(range(n, 0, -1))
    middle_rod = []
    bottom_rod = []
    def move_disks(num, source, target, extra):
        if num == 1:
            target.append(source.pop())
            ans.append(f"{top_rod} {middle_rod} {bottom_rod}")
        else:
            move_disks(num-1, source, extra, target)
            move_disks(1, source, target, extra)
            move_disks(num-1, extra, target, source)
    ans.append(f"{top_rod} {middle_rod} {bottom_rod}")
    move_disks(n, top_rod, bottom_rod, middle_rod)
    return "\n".join(ans)
