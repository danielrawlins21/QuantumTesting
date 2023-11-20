from scipy import signal

f = [[1,2,1],[2,1,1],[1,1,1]]
g = [[1,0.5],[0.5,1]]

conv = signal.convolve2d(f,g,mode='valid')

print(conv)

print(sum(conv))