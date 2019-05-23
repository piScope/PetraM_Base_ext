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

}// namespace PetraM_Base_extra
