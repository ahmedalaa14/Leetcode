func isSubsequence(s string, t string) bool {
    // edge case
\tif len(s) == 0 {
\t\treturn true
\t}

\ti, j := 0, 0

\tfor ; j < len(t); j++ {
\t\tif i < len(s) && t[j] == s[i] {
\t\t\ti++
\t\t}
\t}

\tif i == len(s) {
\t\treturn true
\t}

\treturn false
}