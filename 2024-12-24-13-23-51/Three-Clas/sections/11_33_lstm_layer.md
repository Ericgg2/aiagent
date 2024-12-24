
RNNs are particularly suited for handling linear sequence data, incorporating a recurrent structure within neural networks so that the current hidden layer is influenced not only by the input layer but also by the previous time step. To address the issues of vanishing and exploding gradients, LSTMs introduce storage and memory functions, controlling information flow through gating mechanisms, selectively forgetting some information. An LSTM unit includes an input gate, forget gate, output gate, and memory cell, as depicted in Figure 1.

![](_page_4_Figure_5.jpeg)

Figure 1: Diagram of RNN and LSTM cell structures

Forget Gate: Determines what information should be discarded from the current memory cell. The formula, translated into R-like syntax, is:

$$f_{t}=\sigma(W_{f}\cdot[h_{t-1},x_{t}]+b_{f})\tag{1}$$

![](_page_5_Figure_0.jpeg)

Figure 2: Forget Gate

Input Gate: Decides what new information should be stored in the current memory cell. The formulas, in R-like syntax, are:

$$i_{t}=\sigma(W_{i}\cdot[h_{t-1},x_{t}]+b_{i})\tag{2}$$

$$\tilde{c}_{t}=\tanh(W_{c}\cdot[h_{t-1},x_{t}]+b_{c})\tag{3}$$

Update Memory Cell: Updates the state of the current memory cell. The formula, in R-like syntax, is:

$$c_{t}=f_{t}\times c_{t-1}+i_{t}\times\tilde{c}_{t}\tag{4}$$

![](_page_6_Figure_0.jpeg)

Figure 3: ct

Output Gate: Determines what part of the current memory cell should be output. The formulas, in R-like syntax, are:

$$O_{t}=\sigma(W_{o}\cdot[h_{t-1},x_{t}]+b_{o})\tag{5}$$

$h_{t}=O_{t}\times\tanh(c_{t})$

![](_page_7_Figure_0.jpeg)

Figure 4: Output Gate

![](_page_7_Figure_2.jpeg)

Figure 5: LSTM
