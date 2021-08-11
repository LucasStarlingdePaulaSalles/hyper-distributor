# Quantitative Information Flow Hyper Distribution Calculator
$$
|\mathcal{X}| = 3
$$
$$
|\mathcal{Y}| = 3
$$

$$
\pi = \{0.33333, 0.33333, 0.33333, \}
$$

## Channel F matrix
$$
\begin{array}{|c|ccc|}
\hline
\mathsf{F} & y_1 & y_2 & y_3 \\ \hline
x_1 & 0.4 & 0.0 & 0.6 \\
x_2 & 0.1 & 0.75 & 0.15 \\
x_3 & 0.2 & 0.5 & 0.3 \\
\hline
\end{array}
$$

## Joint matrix
$$
\begin{array}{|c|ccc|}
\hline
\mathsf{J} & y_1 & y_2 & y_3 \\ \hline
x_1 & 0.1333 & 0.0 & 0.2 \\
x_2 & 0.0333 & 0.25 & 0.05 \\
x_3 & 0.0667 & 0.1667 & 0.1 \\
\hline
\end{array}
$$

$$
p_\mathsf{Y} = \{0.23333, 0.41667, 0.35, \}
$$

## Posterior matrix
$$
\begin{array}{|c|c|c|c|}
\hline
\ & P[ \mathcal{X} | y_{1}] & P[ \mathcal{X} | y_{2}] & P[ \mathcal{X} | y_{3}] \\ \hline
x_1 & 0.5714 & 0.0 & 0.5714 \\
x_2 & 0.1429 & 0.6 & 0.1429 \\
x_3 & 0.2857 & 0.4 & 0.2857 \\
\hline
\end{array}
$$

## Hyper Distribution
$$
\begin{array}{|c|c|c|}
\hline
[\pi \vartriangleright \mathsf{F}] & 0.417 & 0.583 \\ \hline
x_1 & 0.0 & 0.5714 \\
x_2 & 0.6 & 0.1429 \\
x_3 & 0.4 & 0.2857 \\
\hline
\end{array}
$$

