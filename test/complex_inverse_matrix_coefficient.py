import numpy as np
from scipy.linalg import inv

from mfem import mfem_mode
if mfem_mode == 'parallel':
    import mfem.par as mfem
else:
    import mfem.ser as mfem    

test_matrix1 = np.diag([1]*5).astype(complex)
test_matrix2 = np.diag([1]*5) + 1j*np.diag([1]*5)
test_matrix3= (np.random.rand(16) + 1j*np.random.rand(16)).reshape(4,4)

def do_test(m, Tr, ip):
    M1 = mfem.DenseMatrix(*(m.shape))
    M1.Assign(m.real)
    M2 = mfem.DenseMatrix(*(m.shape))
    M2.Assign(m.imag)

    cM1 = mfem.MatrixConstantCoefficient(M1)
    cM2 = mfem.MatrixConstantCoefficient(M2)    
    
    from petram.ext.base import ComplexInverseMatrixCoefficient

    Ans = mfem.DenseMatrix(*(m.shape))
    
    cimc1 = ComplexInverseMatrixCoefficient(cM1, cM2, 1)
    cimc2 = ComplexInverseMatrixCoefficient(cM1, cM2, 0)

    cimc1.Eval(Ans, Tr, ip)
    Re = Ans.GetDataArray().copy()
    cimc2.Eval(Ans, Tr, ip)
    Im = Ans.GetDataArray().copy()

    ans = Re + 1j*Im
    ref = inv(m)
    print("ans", ans)
    print("reference", ref)

    error =np.max(np.abs(ans-ref).flatten())
    print("error", error)
    check = error  < 1e-14
    return check
    
def test():

    # make a sample mesh
    tri_v = [[0., -1.,  0.], [0.,  0.,  1.], [ 0.,  0., -1.]]
    tri_e = [[0, 1, 2],]

    Nvert = len(tri_v)
    Nelem = len(tri_e)
    mesh = mfem.Mesh(2, Nvert, Nelem, 0, 3)
    
    for j in range(Nvert):
        mesh.AddVertex(tri_v[j])
    for j in range(Nelem):
        mesh.AddTriangle(tri_e[j], j+1)
        
    mesh.FinalizeTriMesh(1,1, True)

    # define L2 finite element space
    fec = mfem.L2_FECollection(1, mesh.Dimension())
    fes = mfem.FiniteElementSpace(mesh, fec, mesh.SpaceDimension())

    el = fes.GetFE(0)
    Tr = fes.GetElementTransformation(0)    
    
    ir = mfem.IntRules.Get(el.GetGeomType(), 1)
    ip = ir.IntPoint(0)

    result = [do_test(test_matrix1, Tr, ip),
              do_test(test_matrix2, Tr, ip),
              do_test(test_matrix3, Tr, ip)]

    if not all(result):
        print("(fail) ComplexInversrMatrixCoefficient")
              
    return all(result)


if __name__ == "__main__":
   test()
    
