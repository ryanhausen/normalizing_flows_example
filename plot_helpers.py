
import matplotlib.pyplot as plt
import numpy as np


# https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html
def scatter_hist(dist, x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    
    vals = ax.scatter(x, y, c="tab:blue", marker="o", alpha=0.5)
    ax.annotate("Joint", (0.02, 0.97), xycoords="axes fraction")
    ax.set_ylabel("$Y$")
    ax.set_xlabel("$X$")
    
    ax_histx.hist(x, bins=bins, density=True)
    ax_histx.annotate("Marginal X", (0.02, 0.90), xycoords="axes fraction")
    
    ax_histy.hist(y, bins=bins, orientation='horizontal', density=True)
    ax_histy.annotate("Marginal Y", (0.05, 0.97), xycoords="axes fraction")

    #y_min, y_max = ax.get_ylim()
    #x_min, x_max = ax.get_xlim()
    #xs, ys = np.meshgrid(np.linspace(x_min, x_max, num=100), np.linspace(y_min, y_max, num=100))
    #vals = np.array([[y, x] for y, x in zip(ys.flatten(), xs.flatten())], dtype=np.float32)
    #zs = dist.prob(vals).numpy().reshape([100, 100])
    #ax.contour(xs, ys, zs, alpha=0.5, cmap="jet")

def hist2d_marginals(dist, x, y):
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    spacing = 0.005


    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom + height + spacing, width, 0.2]
    rect_histy = [left + width + spacing, bottom, 0.2, height]

    # start with a square Figure
    fig = plt.figure(figsize=(8, 8))

    ax = fig.add_axes(rect_scatter)
    ax_histx = fig.add_axes(rect_histx, sharex=ax)
    ax_histy = fig.add_axes(rect_histy, sharey=ax)

    # use the previously defined function
    scatter_hist(dist, x, y, ax, ax_histx, ax_histy)

    plt.show()
    
    
def hist_with_pdf(samples, dist):
    plt.figure(figsize=(10,5))
    xs = np.linspace(-5.0, 5.0, num=100)
    plt.plot(xs, dist.prob(xs), label="pdf")
    plt.hist(samples.numpy(), density=True, bins=100, label="samples")
    plt.legend()
    plt.show()
    
