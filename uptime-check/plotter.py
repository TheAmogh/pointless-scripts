import matplotlib.pyplot as plt
import time
import bisect


def plot(filename, start_time=None, end_time=None):
    X, Y = fetch_data(filename)

    if not start_time:
        plot_X_Y(X, Y)
        return

    # Assume X is in ascending order and apply binary search for start_time and end_time
    start_index = bisect.bisect_left(X, start_time)
    end_index = bisect.bisect_right(X, end_time)

    plt.plot([start_time, end_time], [0, 0], 'rx')
    plot_X_Y(X[start_index:end_index], Y[start_index:end_index])


def fetch_data(filename):
    X, Y = [], []
    with open(filename) as myfile:
        for line in myfile:
            x, y = line.strip().split(',')
            X.append(int(float(x)))
            Y.append(int(y))

    return X, Y


def plot_X_Y(X, Y):
    plt.plot(X, Y, '.')
    plt.show()


if __name__ == '__main__':
    ONE_HOUR = 60 * 60
    ONE_DAY = ONE_HOUR * 24
    current_time = time.time()
    plot('ping.log', current_time-ONE_DAY, current_time)
