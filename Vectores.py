def suma_vec(V,W):
  if isinstance(V,list) and isinstance(W,list):
    if len(V)==len(W):
      return aux_suma_vec(V,W,0,len(V),[])
    else:
      return "El tamaño de los vectores debe ser igual"
  else:
    return "Las entradas deben de ser de tipo lista"

def aux_suma_vec(V,W,i,N,R):
  if i == N:
    return R
  else:
    R+= [V[i]+W[i]]
    return aux_suma_vec(V,W,i+1,N,R)
  
###############################################################################
  
def producto_escalar(V,K):
  if isinstance(V,list):
    if isinstance(K,int) or isinstance(K,float):
      return aux_producto_escalar(V,K,0,len(V),V)
    else:
      return "El paráetro K debe ser un número real"
  else:
    return "El parámetro V debe ser de tipo lista"

def aux_producto_escalar(V,K,i,N,R):
  if i == N:
    return R
  else:
    R[i]*=K
    return aux_producto_escalar(V,K,i+1,N,R)
  
###############################################################################
  
def producto_punto(V,W):
  if isinstance(V,list) and isinstance(W,list):
    if len(V)==len(W):
      return aux_producto_punto(V,W,0,len(V),0)
    else:
      return "El tamaño de los vectores debe ser igual"
  else:
    return "Las entradas deben de ser de tipo lista"

def aux_producto_punto(V,W,i,N,R):
  if i == N:
    return R
  else:
    R+= V[i]*W[i]
    return aux_producto_punto(V,W,i+1,N,R)
  
###############################################################################

def suma_matrices(M1,M2):
  if isinstance(M1,list) and isinstance(M2,list):
    if len(M1)==len(M2)and len(M1[0])==len(M2[0]):
      return aux_suma_matrices(M1,M2,len(M1),len(M1[0]),0,0,M1)
    else:
      return "Las matrices deben ser del mismo largo"
  else:
    return "Las matrices deben ser listas"
def aux_suma_matrices(M1,M2,m,n,i,j,R):
  if i==m:
    return R
  elif j==n:
    return aux_suma_matrices(M1,M2,m,n,i+1,0,R)
  else:
    R[i][j]+=M2[i][j]
    return aux_suma_matrices(M1,M2,m,n,i,j+1,R)
  
###############################################################################
  
def suma_matrices2(M1,M2):
  if isinstance(M1,list) and isinstance(M2,list):
    if len(M1)==len(M2)and len(M1[0])==len(M2[0]):
      return aux_suma_matrices2(M1,M2,len(M1),len(M1[0]),0,0,[],[])
    else:
      return "Las matrices deben ser del mismo largo"
  else:
    return "Las matrices deben ser listas"
def aux_suma_matrices2(M1,M2,m,n,i,j,Vec,Matr):
  if i==n:
    return Matr
  elif j==m:
    Matr.append(Vec)
    return aux_suma_matrices2(M1,M2,m,n,i+1,0,[],Matr)
  else:
    Vec.append(M1[i][j]+M2[i][j])
    return aux_suma_matrices2(M1,M2,m,n,i,j+1,Vec,Matr)

###############################################################################

def traspuesta_matriz(M):
  if isinstance(M,list):
    if len(M)==len(M[0]):
      return traspuesta_matriz_aux(M,len(M),len(M[0]),0,0,[],[])
    else:
      return "Las filas y columnas deben ser del mismo largo"
  else:
    return "La matriz debe ser una lista"

def traspuesta_matriz_aux(M,n,m,i,j,V,R):
  if j==n:
    return R
  elif i==m:
    R.append(V)
    return traspuesta_matriz_aux(M,n,m,0,j+1,[],R)
  else:
    V.append(M[i][j])
    return traspuesta_matriz_aux(M,n,m,i+1,j,V,R)
  
###############################################################################

def mult_vec_mat(V,M):
  if len(V)==len(M[0]):
    return mult_vec_mat_aux(V,traspuesta_matriz(M),len(M),len(M[0]),0,0,0,[])
  else:
    return "Error"
def mult_vec_mat_aux(V,M,n,m,i,j,Suma,R):
  if i==n:
    return R
  elif j==m:
    R.append(Suma)
    return mult_vec_mat_aux(V,M,n,m,i+1,0,0,R)
  else:
    Suma+=V[i]*M[i][j]
    return mult_vec_mat_aux(V,M,n,m,i,j+1,Suma,R)
  
###############################################################################
  
def mult_matrices(M1,M2):
  if len(M1[0])==len(M2):
    return aux_mult_matrices(M1,M2,len(M1),0,[])
  else:
    return "Error"

def aux_mult_matrices(M1,M2,n,i,R):
  if i==n:
    return R
  else:
    R.append(mult_vec_mat(M1[i],M2))
    return aux_mult_matrices(M1,M2,n,i+1,R)
