if __name__ == '__main__':
    (_, h) = (int(input()),set(map(int, input().split())))
    r = int(input())
    for _ in range(r):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(h, command)(newSet)

    print (sum(h))
