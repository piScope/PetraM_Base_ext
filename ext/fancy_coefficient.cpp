#include "mfem.hpp"
#include "fancy_coefficient.hpp"
#include <iostream>

using namespace mfem;

namespace PetraM_Base_extra
{

double PiecewiseLinearMaterialProperty::Eval(ElementTransformation &T,
					       const IntegrationPoint &ip){

  double cfv, ans = 0.0;
  cfv = cf -> Eval(T, ip);
  
  const Vector &x = *_x;
  const Vector &y = *_y;

  int size = _x -> Size();

  if (x[0] > cfv) {
    if (range_check == 1){
      mfem_error("PiecewiseLinearMaterialProperty::out of range  \n");
    } else {
      return y[0];
    }
  }
  if (x[size-1] < cfv) {
    if (range_check == 1){    
      mfem_error("PiecewiseLinearMaterialProperty::out of range  \n");
    } else {
      return y[size - 1];
    }
  }
  
  for (int i = 0; i < size; i++) {
    if ((x[i] <= cfv) && (cfv < x[i+1])){
      ans = y[i+1]*(cfv-x[i])/(x[i+1]- x[i]) + y[i]*(x[i+1]-cfv)/(x[i+1]-x[i]);
      //std::cout << cfv << ":" << i<< ":" << ans << "\n";
      return ans;
    }	
  }
  mfem_error("PiecewiseLinearMaterialProperty::??? (should not come here ;D \n");  
  return 0.0;

}
double Poly1DMaterialProperty::Eval(ElementTransformation &T,
					    const IntegrationPoint &ip){
  double cfv, ans = 0.0, term = 1.;
  cfv = cf -> Eval(T, ip);
  
  const Vector &coeff = *_coeff;

  int size = _coeff -> Size();

  if (max_range > cfv) {
    mfem_error("Poly1DMaterialProperty::out of range  \n");
  }
  if (min_range < cfv) {
    mfem_error("Poly1DMaterialProperty::out of range  \n");
  }


  for (int i = 0; i < size; i++) {
      ans = ans + coeff[i]*term;
      term = term * cfv;
  }
  return ans;
}
void UniaxialConstantMaterialProperty::Eval(DenseMatrix &K, ElementTransformation &T,
					      const IntegrationPoint &ip){

  mfem_error("Not Implemented");
}

ComplexInverseMatrixCoefficient::ComplexInverseMatrixCoefficient(MatrixCoefficient &ReA, MatrixCoefficient &ImA, int real)
  : MatrixCoefficient(ReA.GetHeight(), ReA.GetWidth()), _ReA(&ReA), _ImA(&ImA), _real(real),
    Ms(ReA.GetHeight(),ReA.GetWidth()), Mbig(ReA.GetHeight()*2,ReA.GetWidth()*2)
{
   MFEM_ASSERT(ReA.GetHeight() == ReA.GetWidth(),
               "ComplexInverseMatrixCoefficient:  "
               "Argument must be a square matrix.");
   MFEM_ASSERT(ImA.GetHeight() == ImA.GetWidth(),
               "ComplexInverseMatrixCoefficient:  "
               "Argument must be a square matrix.");
   MFEM_ASSERT(ImA.GetHeight() == ReA.GetWidth(),
               "ComplexInverseMatrixCoefficient:  "
               "Real and Imag must be the same size.");   
}
  
void ComplexInverseMatrixCoefficient::Eval(DenseMatrix &M, ElementTransformation &T,
					   const IntegrationPoint &ip){

  /*
     compute 
      [A -B] 
      [B  A]
  */
   int c, r,  n = Ms.Width();
   
   _ReA->Eval(Ms, T, ip);
   for (c = 0; c < n; c++){
     for (r = 0; r < n; r++){
       Mbig(r, c) = Ms(r, c);
     }
   }
   for (c = 0; c < n; c++){
     for (r = 0; r < n; r++){
       Mbig(r+n, c+n) = Ms(r, c);
     }
   }
   _ImA->Eval(Ms, T, ip);   
   for (c = 0; c < n; c++){
     for (r = 0; r < n; r++){
       Mbig(r+n, c) = Ms(r, c);
     }
   }
   for (c = 0; c < n; c++){
     for (r = 0; r < n; r++){
       Mbig(r, c+n) = -Ms(r, c);
     }
   }
   
   Mbig.Invert();

   if (_real) {
     for (c = 0; c < n; c++){
       for (r = 0; r < n; r++){
	 M(r, c) = Mbig(r, c);
       }
     }
   } else {
     for (c = 0; c < n; c++){
       for (r = 0; r < n; r++){
	 M(r, c) = -Mbig(r, c+n);
       }
     }     
   }
}
  
MatrixSliceCoefficient::MatrixSliceCoefficient(MatrixCoefficient &A, Array<int> rindex, Array<int> cindex)
  : MatrixCoefficient(cindex.Size(), rindex.Size()), _A(&A), Mtmp(A.GetHeight(), A.GetWidth()),
    _rindex(rindex), _cindex(cindex)
{
  
  for (int i=0; i < _rindex.Size(); i++){
    MFEM_ASSERT(_rindex[i] < A.GetWidth(),
		"MatrixSliceCoefficient: "
		"row index must smaller than the width.");
  }
  for (int j=0; j < _cindex.Size(); j++){
    MFEM_ASSERT(_cindex[j] < A.GetHeight(),
		"MatrixSliceCoefficient: "
		"column index must smaller than the height.");
  }
}

void MatrixSliceCoefficient::Eval(DenseMatrix &M, ElementTransformation &T,
					   const IntegrationPoint &ip){

  _A->Eval(Mtmp, T, ip);  
  for (int i=0; i < _rindex.Size(); i++){
    for (int j=0; j < _cindex.Size(); j++){
       M(i, j) = Mtmp(_rindex[i], _cindex[j]);      
    }
  }
}

  
}// namespace PetraM_Base_extra
