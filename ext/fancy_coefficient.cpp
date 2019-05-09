#include "mfem.hpp"
#include "fancy_coefficient.hpp"

using namespace mfem;

namespace PetraM_Base_extra
{

double Scalar_PiecewiseLinear_MaterialProperty::Eval(ElementTransformation &T,
					       const IntegrationPoint &ip){

  double gfv;
  gfv = GridF -> GetValue (T.ElementNo, ip, 0.0);
  return gfv;

}
double Scalar_Poly1D_MaterialProperty::Eval(ElementTransformation &T,
					    const IntegrationPoint &ip){

  return 0.0;
}
void Uniaxial_constant_MaterialProperty::Eval(DenseMatrix &K, ElementTransformation &T,
					      const IntegrationPoint &ip){

  mfem_error("Not Implemented");
}

}// namespace PetraM_Base_extra
