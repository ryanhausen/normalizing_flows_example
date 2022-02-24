
import matplotlib.pyplot as plt
import numpy as np


# https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html
def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # the scatter plot:

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    
    vals = ax.hist2d(x, y, bins=bins, cmap="Blues", density=True)
    ax.annotate("Joint", (0.02, 0.97), xycoords="axes fraction")
    ax.set_ylabel("$Y$")
    ax.set_xlabel("$X$")
    cbar = plt.colorbar(vals[-1])
    cbar.ax.set_ylabel("P($X$,$Y$)")
    
    ax_histx.hist(x, bins=bins, density=True)
    ax_histx.annotate("Marginal X", (0.02, 0.90), xycoords="axes fraction")
    
    ax_histy.hist(y, bins=bins, orientation='horizontal', density=True)
    ax_histy.annotate("Marginal Y", (0.05, 0.97), xycoords="axes fraction")

def hist2d_marginals(x, y):
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
    scatter_hist(x, y, ax, ax_histx, ax_histy)

    plt.show()
    
    
def hist_with_pdf(samples, dist):
    plt.figure(figsize=(10,5))
    xs = np.linspace(-5.0, 5.0, num=100)
    plt.plot(xs, dist.prob(xs), label="pdf")
    plt.hist(samples.numpy(), density=True, bins=100, label="samples")
    plt.legend()
    plt.show()
    
