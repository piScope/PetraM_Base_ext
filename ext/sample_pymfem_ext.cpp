#include "sample_pymfem_ext.hpp"

using namespace sample_PyMFEM_ext_ns;

sample_PyMFEM_ext::sample_PyMFEM_ext(int refine_)
{
      this -> refine = refine_;
      std::cout << "Conctructor called" << std::endl;
}

sample_PyMFEM_ext::~sample_PyMFEM_ext()
{
      std::cout << "Destructor called" << std::endl;
}

void sample_PyMFEM_ext::call_refine(mfem::Mesh *mesh)
{
  for (int l = 0; l < refine; l++)
   {
      mesh->UniformRefinement();
   }
}
int sample_PyMFEM_ext::get_refine(void) {
  return this->refine;
}
