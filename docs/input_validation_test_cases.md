# GeneWeaver - Input Validation Test Cases

## Day 09: Input Validation and Edge Cases

### Objective
To identify and document invalid and unusual FASTA input
conditions that should be handled by GeneWeaver.

### Test Cases

| Test ID | Test Scenario | Expected Behavior |
|---------|---------------|-------------------|
| TC01 | Valid FASTA input | Accept input |
| TC02 | Invalid DNA characters | Reject invalid sequence |
| TC03 | Empty FASTA sequence | Handle validation error |
| TC04 | Missing input file | Display clear error |
| TC05 | Multiple target sequences | Process all targets |
| TC06 | Target shorter than guide | Return no matching window |
| TC07 | Invalid sequence format | Display clear error |
| TC08 | Zero mismatch threshold | Find exact matches only |

### Validation Areas

1. FASTA input validation
2. DNA sequence validation
3. Empty sequence handling
4. File existence checking
5. Target sequence length checking
6. Error handling

### Conclusion

Day 09 focuses on documenting input validation
and edge-case scenarios to improve GeneWeaver's
reliability and testing coverage.