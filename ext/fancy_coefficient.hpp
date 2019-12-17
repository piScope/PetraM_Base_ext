/*

   FancyCoefficient

   * Add class to define more complicated coefficient
   

   * We use MaterialProperty in naming instead of Coefficient.
     When these classes are moved to main mfem, we envision
     that MaterialProperty will be replaced to Coefficient.


   * PiecewiseLinearMaterialProperty
        PiecewiseLinearMaterialProperty(f, m, n)

        output = interp1d(m, n, "linear")(f(x, y, z))
    
   * Poly1DMaterialProperty 
   * UniaxialConstantMaterialProperty
 */

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
  
  class PiecewiseLinearMaterialProperty : public Coefficient
  {
  private:
    Coefficient  *cf;
    const Vector       *_x;
    const Vector       *_y;
    int          range_check=1;
  public:
     PiecewiseLinearMaterialProperty(Coefficient *_cf,
				     const Vector &x,
				     const Vector &y ) :
      cf(_cf),
      _x(new Vector(x)),
      _y(new Vector(y)) {}
    PiecewiseLinearMaterialProperty(GridFunction *_gf,
				    const Vector &x,
				    const Vector &y,
				    int comp=1):
      cf(new GridFunctionCoefficient(_gf, comp)),
      _x(new Vector(x)),
      _y(new Vector(y)) {}

    void SetRangeCheck(int f){range_check=f;}
    virtual double Eval(ElementTransformation &T,
			const IntegrationPoint &ip);
    
    ~PiecewiseLinearMaterialProperty() {
         delete _x;
	 delete _y;
    }
  };
    
  /// Scalar material property dependent on 1D interpolated
  /// function
  
  class Poly1DMaterialProperty : public Coefficient
  {
  private:
    Coefficient  *cf;
    Vector       *_coeff;
    double       max_range, min_range;
  public:
    Poly1DMaterialProperty(Coefficient *_cf,
			   const Vector &coeff,
			   double _max_range = std::numeric_limits<double>::infinity(),
			   double _min_range = -std::numeric_limits<double>::infinity()):
      cf(_cf),
      _coeff(new Vector(coeff)),      
      max_range(_min_range),
      min_range(_max_range) {}
      
    Poly1DMaterialProperty(GridFunction *_gf,
			   const Vector &coeff,
			   int comp=1,
			   double _max_range = std::numeric_limits<double>::infinity(),
			   double _min_range = -std::numeric_limits<double>::infinity()):    
      cf(new GridFunctionCoefficient(_gf, comp)),
      _coeff(new Vector(coeff)),      
      max_range(_min_range),
      min_range(_max_range) {}
      
    virtual double Eval(ElementTransformation &T,
			const IntegrationPoint &ip);
    

  };
  
  class UniaxialConstantMaterialProperty: public MatrixCoefficient
  {
  private:
    Coefficient  *cf;        
    DenseMatrix mat;  
    double              n_para;
    double              n_perp;    
  public:
    UniaxialConstantMaterialProperty (Coefficient *_cf, const DenseMatrix &m)
        : MatrixCoefficient(m.Height(), m.Width()), mat(m) { cf = _cf;}
    UniaxialConstantMaterialProperty (GridFunction *_gf, const DenseMatrix &m, int comp=1)
      : MatrixCoefficient(m.Height(), m.Width()), mat(m) { cf = new GridFunctionCoefficient(_gf, comp);}
    virtual void Eval(DenseMatrix &K, ElementTransformation &T,
		      const IntegrationPoint &ip);

    

  };

  class ComplexInverseMatrixCoefficient : public MatrixCoefficient
  {
  private:
    MatrixCoefficient * _ReA;
    MatrixCoefficient * _ImA;
    mutable DenseMatrix Mbig;  
    mutable DenseMatrix Ms;    
    const int _real;
  public:
    ComplexInverseMatrixCoefficient(MatrixCoefficient &ReA, MatrixCoefficient &ImA,
				    const int return_real);
    virtual void Eval(DenseMatrix &M, ElementTransformation &T,
		      const IntegrationPoint &ip);
    
  };
    
  class MatrixSliceCoefficient : public MatrixCoefficient
  {
  private:
    MatrixCoefficient * _A;
    mutable DenseMatrix Mtmp;      
    const Array<int> _rindex, _cindex;
  public:
    MatrixSliceCoefficient(MatrixCoefficient &A, Array<int> rindex, Array<int> cindex);
    virtual void Eval(DenseMatrix &M, ElementTransformation &T,
		      const IntegrationPoint &ip);
    
  };
  
} /* end of namespace */

#endif


