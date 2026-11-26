#include <cuda_runtime.h>
#include <cstdio>

// Device-Funktion für einen einzelnen 3D-Vektor
__device__ __host__ inline float3 crossProduct(const float3& a, const float3& b) {
    return make_float3(
        a.y * b.z - a.z * b.y,
        a.z * b.x - a.x * b.z,
        a.x * b.y - a.y * b.x
    );
}

// CUDA-Kernel für ein Array von N Vektoren
__global__ void crossProductKernel(const float3* a, const float3* b, float3* c, int n) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n) {
        c[idx] = crossProduct(a[idx], b[idx]);
    }
}

int main() {
    const int N = 1024;
    size_t bytes = N * sizeof(float3);

    // Host-Speicher allokieren
    float3 *h_a = new float3[N];
    float3 *h_b = new float3[N];
    float3 *h_c = new float3[N];

    for (int i = 0; i < N; ++i) {
        h_a[i] = make_float3(1.0f, 0.0f, 0.0f);
        h_b[i] = make_float3(0.0f, 1.0f, 0.0f);
    }

    // Device-Speicher allokieren
    float3 *d_a, *d_b, *d_c;
    cudaMalloc(&d_a, bytes);
    cudaMalloc(&d_b, bytes);
    cudaMalloc(&d_c, bytes);

    // Daten auf die GPU kopieren
    cudaMemcpy(d_a, h_a, bytes, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, bytes, cudaMemcpyHostToDevice);

    // Kernel starten
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
    crossProductKernel<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, N);

    // Ergebnis zurück auf den Host kopieren
    cudaMemcpy(h_c, d_c, bytes, cudaMemcpyDeviceToHost);

    // Ausgabe des ersten Ergebnisses: (0, 0, 1)
    
    // Speicher freigeben
    cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);
    
    return 0;
}
