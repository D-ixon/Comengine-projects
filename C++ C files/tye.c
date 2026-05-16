#include <stdio.h>
#include <stdint.h> // Required header

int main() {
    int32_t regular_score = -500; // Can be negative
    uint64_t massive_crypto_wallet = 15000000000000000000ULL; // Positive only, ultra large

    printf("Size of int32_t: %zu bytes\n", sizeof(regular_score));    // Always prints 4
    printf("Size of uint64_t: %zu bytes\n", sizeof(massive_crypto_wallet)); // Always prints 8

    return 0;
}
