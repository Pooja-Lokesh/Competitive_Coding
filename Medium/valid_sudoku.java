class Solution {
    /*
    Idea: 
    we are storing all elements belongs to row i in rows[i] set and
                   all elements belongs to col i in cols[i] set and
                   all elements belongs to sub-box i in sub[i] set
            So Every time before we add element to respective sets we check if already exists
                if exists means its repeating on a row or column or sub-box so return false.
                otherwise after adding all elements return true.
    
    */
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] rows = new Set[9];
        Set<Character>[] cols = new Set[9];
        Set<Character>[] sub = new Set[9];
        for(int i=0;i<9;i++)
        {
            if(rows[i]==null){
                rows[i] = new HashSet<Character>();
            }
            for(int j=0;j<9;j++)
            {
                if(cols[j]==null){
                    cols[j] = new HashSet<Character>();
                }
                if(board[i][j]!='.'){
                    int c = i/3 * 3 + j/3;
                    if(sub[c]==null){
                        sub[c] = new HashSet<Character>();
                    }
                    char e = board[i][j];
                    if(rows[i].contains(e) || cols[j].contains(e) || sub[c].contains(e)){
                        return false;
                    }
                    rows[i].add(board[i][j]);
                    cols[j].add(board[i][j]);
                    sub[c].add(board[i][j]);
                }
            }
        }
        return true;
    }
}