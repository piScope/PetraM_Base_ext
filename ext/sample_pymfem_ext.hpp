#ifndef PYMFEM_EXC_SAMPLE_H
#define PYMFEM_EXC_SAMPLE_H

#include <stdio.h>
#include <string.h>
#include "mfem.hpp"

namespace sample_PyMFEM_ext_ns
{
class sample_PyMFEM_ext
{
 private:
  int  refine = 1;
  
 public:
  sample_PyMFEM_ext(int refine_ = 1);
  ~sample_PyMFEM_ext();
  void call_refine(mfem::Mesh *mesh);
  int  get_refine(void);
};
  
} /* end of namespace */

#endif


