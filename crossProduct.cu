#include <cuda_runtime.h>
#include <cstdio>
// kaputt ,060
// forlaufend ,065
// versetzt 0,57
// Device/GPU-Funktion
__global__ void crossProductKernel(const float* a, const float* b, float* c, int n) {
    // eindeutigen Index des aktuellen Threads berechenen (Nummer des eigenen Blocks * gemeinsame Blockgroesse + Position im eigenen Block)
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    
    // i ist eine grösse zwischen 0 und 1024 und soll diesen Bruchteil einer Mio berechnen (abfolgend oder um 1024 versetzt?)
    // abfolgend: von i*1024 bis (i+1)*1024, +1, aber was für das ende!!
    // versetzt: von i * 1024 bis 1Mio, +1024
    for (int k=i*1024;( k <n);k+=1024) {
//    for (int k=i*1024;( k < (i+1)*1024 & k<n);k++) {
//    if (i<n){
        // Der Index im Array fuer 3D-Vektoren ist k * 3
        int idx = k * 3;
        int idy = idx + 1;
        int idz = idx + 2;
        
        c[idx] = a[idy] * b[idz] - a[idz] * b[idy];
        c[idy] = a[idz] * b[idx] - a[idx] * b[idz];
        c[idz] = a[idx] * b[idy] - a[idy] * b[idx];
    }
    }
__host__ int main(){

    int n=1000000;
    float *a = new float[3*n];
    float *b = new float[3*n];
    float *c = new float[3*n];
    for (int i=0;i<n;i++){
        a[i]= ((float)rand()/(float)(RAND_MAX)) * 5.0f;
        b[i]= ((float)rand()/(float)(RAND_MAX)) * 5.0f;
    }

    float *a_device, *b_device, *c_device;
    // GPU-Speicher schreiben
    cudaMalloc(&a_device, 3*n*sizeof(float));
    cudaMalloc(&b_device, 3*n*sizeof(float));
    cudaMalloc(&c_device, 3*n*sizeof(float));

    cudaMemcpy(a_device, a, 3*n*sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(b_device, b, 3*n*sizeof(float), cudaMemcpyHostToDevice);
    
    // Blockgroesse
    int threadsPerBlock = 256;
    // benoetigte Blockzahl (aufgerundet)
    int blocksPerGrid = ceil(n / threadsPerBlock);
   
    // Kernelaufruf, startet mittelbar 1024 Threads in 4 Bloecken
    crossProductKernel<<<blocksPerGrid, threadsPerBlock>>>(a, b, c, n);

    //GPU-Speicher lesen und loeschen
    cudaMemcpy(c_device, c, 3*n*sizeof(float), cudaMemcpyDeviceToHost);
        
    free(a);
    free(b);
    free(c);
    cudaFree(a_device);
    cudaFree(b_device);
    cudaFree(c_device);
}
