While Large Language models represent advanced reasoning tools, they still en-
counter a number of issues when faced with logical and mathematical problems.
To tackle this issue, we propose a solution that combines argumentation theories
and the test-time compute inference paradigm. The latter can be encapsulated
by the idea of giving the model more ‘time to think’ before providing an output.
The former refers to Toulmin’s tradition of argumentative pattern components
and the notion of critical questions that serve to probe arguments’ validity. Our
solution merges all such elements into a pipeline, denoted as Critical-Questions-
of-Thought (CQoT), capable of enhancing LLMs reasoning performances. We
assessed CQoT on the MT-Bench Reasoning and Math questions, testing it with
five different models, proprietary and open source. The evaluation resulted in
CQoT outperforming both the baseline model and its version augmented by
Chain-of-Thought, exhibiting an average 5% improvement in response correct-
ness and helpfulness.
Acknowledgment
We are grateful to the UK Materials and Molecular Modelling Hub for com-
putational resources, which is partially funded by EPSRC (EP/T022213/1,
EP/W032260/1 and EP/P020194/1).