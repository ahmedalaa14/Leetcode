func partition(s string) [][]string {
\tvar result [][]string
\tvar curr []string
\tlenS := len(s)

\tvar explore func(index int)
\texplore = func(index int) {
\t\tif index >= lenS {
\t\t\tresult = append(result, append([]string(nil), curr...))
\t\t\treturn
\t\t}

\t\tfor i := index; i < lenS; i++ {
\t\t\tsubStr := s[index : i+1]
\t\t\tif isPalindrome(subStr) {
\t\t\t\tcurr = append(curr, subStr)
\t\t\t\texplore(i + 1)
\t\t\t\tcurr = curr[:len(curr)-1]
\t\t\t}
\t\t}
\t}

\texplore(0)
\treturn result
}

func isPalindrome(s string) bool {
\tleft, right := 0, len(s)-1
\tfor left < right {
\t\tif s[left] != s[right] {
\t\t\treturn false
\t\t}
\t\tleft++
\t\tright--
\t}
\treturn true
}