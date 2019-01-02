input:read0`:input.txt
input:", " vs input[0]

// Part 1
dir:("LR"!-1 1)input[;0];
ds:sums[dir] mod 4;
steps:("J"$1_/:input);
stepdir:(til 4)!(0 1;1 0;0 -1;-1 0);
total:sum steps*stepdir(ds);
answer:sum abs total;
0N!answer

dir:("LR"!-1 1)input[;0];
ds:sums[dir] mod 4;
steps:("J"$1_/:input);
stepdir:(til 4)!(0 1;1 0;0 -1;-1 0);
temp:stepdir(ds);
// #' is a take both-each pairwise thing
total:sums enlist[0 0],raze steps#'enlist each(temp);
answer:sum abs first where 1<count each group total
0N!answer
