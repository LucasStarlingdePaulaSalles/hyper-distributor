# Quantitative Information Flow Hyper Distribution Calculator
$$
|\mathcal{X}| = 3
$$
$$
|\mathcal{Y}| = 4
$$

$$
\pi = \{0.25, 0.5, 0.25, \}
$$

## Channel C matrix
$$
\begin{array}{|c|cccc|}
\hline
\mathsf{C} & y_1 & y_2 & y_3 & y_4 \\ \hline
x_1 & 0.5 & 0.5 & 0.0 & 0.0 \\
x_2 & 0.0 & 0.25 & 0.5 & 0.25 \\
x_3 & 0.5 & 0.3333 & 0.1667 & 0.0 \\
\hline
\end{array}
$$

## Joint matrix
$$
\begin{array}{|c|cccc|}
\hline
\mathsf{J} & y_1 & y_2 & y_3 & y_4 \\ \hline
x_1 & 0.125 & 0.125 & 0.0 & 0.0 \\
x_2 & 0.0 & 0.125 & 0.25 & 0.125 \\
x_3 & 0.125 & 0.0833 & 0.0417 & 0.0 \\
\hline
\end{array}
$$

$$
p_\mathsf{Y} = \{0.25, 0.33333, 0.29167, 0.125, \}
$$

## Posterior matrix
$$
\begin{array}{|c|c|c|c|c|}
\hline
\ & P[ \mathcal{X} | y_{1}] & P[ \mathcal{X} | y_{2}] & P[ \mathcal{X} | y_{3}] & P[ \mathcal{X} | y_{4}] \\ \hline
x_1 & 0.5 & 0.375 & 0.0 & 0.0 \\
x_2 & 0.0 & 0.375 & 0.8571 & 1.0 \\
x_3 & 0.5 & 0.25 & 0.1429 & 0.0 \\
\hline
\end{array}
$$

## Hyper Distribution
$$
\begin{array}{|c|c|c|c|c|}
\hline
[\pi \vartriangleright \mathsf{C}] & 0.292 & 0.125 & 0.333 & 0.25 \\ \hline
x_1 & 0.0 & 0.0 & 0.375 & 0.5 \\
x_2 & 0.8571 & 1.0 & 0.375 & 0.0 \\
x_3 & 0.1429 & 0.0 & 0.25 & 0.5 \\
\hline
\end{array}
$$

