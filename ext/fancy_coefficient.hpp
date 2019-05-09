#ifndef FANCY_COEFFICIENTS_H
#define FANCY_COEFFICIENTS_H

#include <stdio.h>
#include <string.h>
#include "mfem.hpp"

using namespace mfem;

namespace PetraM_Base_extra
{
  /// Scalar material property dependent on 1D interpolated
  /// function
  
  class Scalar_PiecewiseLinear_MaterialProperty : public Coefficient
  {
  private:
    GridFunction *GridF;
    Vector       *x;
    Vector       *y;    
  public:
    Scalar_PiecewiseLinear_MaterialProperty(GridFunction *_gf, Vector *_x, Vector *_y)
					    { GridF = _gf; x = _x, y = _y;}

    void SetGridFunction(GridFunction *gf) { GridF = gf; }
    GridFunction * GetGridFunction() const { return GridF; }
    virtual double Eval(ElementTransformation &T,
			const IntegrationPoint &ip);
    

  };
    
  /// Scalar material property dependent on 1D interpolated
  /// function
  
  class Scalar_Poly1D_MaterialProperty : public Coefficient
  {
  private:
    GridFunction *GridF;
    Vector       *Coeff;
  public:
    Scalar_Poly1D_MaterialProperty(GridFunction *_gf, Vector *_coeff)
      { GridF = _gf; Coeff= _coeff; }	

    void SetGridFunction(GridFunction *gf) { GridF = gf; }
    GridFunction * GetGridFunction() const { return GridF; }
    virtual double Eval(ElementTransformation &T,
			const IntegrationPoint &ip);
    

  };
  
  class Uniaxial_constant_MaterialProperty: public MatrixCoefficient
  {
  private:
    GridFunction *GridF_axis;
    DenseMatrix mat;  
    double              n_para;
    double              n_perp;    
  public:
    Uniaxial_constant_MaterialProperty (GridFunction *_gf, const DenseMatrix &m)
        : MatrixCoefficient(m.Height(), m.Width()), mat(m) { GridF_axis = _gf;}
    void SetGridFunction(GridFunction *gf) { GridF_axis = gf; }
    GridFunction * GetGridFunction() const { return GridF_axis; }
    virtual void Eval(DenseMatrix &K, ElementTransformation &T,
		      const IntegrationPoint &ip);

    

  };
  
} /* end of namespace */

#endif


