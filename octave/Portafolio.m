args = argv();
e1 = str2double(args{1});
e2 = str2double(args{2});
ep = str2double(args{3});

A = [e1 e2; 1 1];
b = [ep; 1];
w = inv(A) * b;

printf("W1=%.6f\nW2=%.6f\n", w(1), w(2));
