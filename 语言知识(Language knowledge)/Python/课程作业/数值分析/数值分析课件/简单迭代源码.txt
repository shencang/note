function [k,p,err,P] = fixpt(g,p0,tol,max1)
% Input - g is the iteration function
%       - p0 is the initial guess for the fixed-point
%       - tol is the tolerance
%       - max1 is the maximum number of iterations
% Output - k is the number of iterations that were carried out
%          - p is the approximation to the fixed-point
%          - err is the error in the approximation
%          - P'contains the sequence {pn}

P(1)= p0;
for k=2:max1
   P(k)=feval(g,P(k-1));
   err=abs(P(k)-P(k-1));
   relerr=err/(abs(P(k))+eps);
   p=P(k);
   if (err<tol) | (relerr<tol),break;end
end

if k == max1
   disp('maximum number of iterations exceeded')
end
P=P';