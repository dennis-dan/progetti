//titolo, autore, num copie e prezzo. tutti i libri hanno 10 copie di default.
public class Libro {
    private String titolo;
    private String autore;
    private int numCopie;

    public Libro(String titolo, String autore) {
        this.titolo = titolo;
        this.autore = autore;
        this.numCopie = 10;
    }

    public String getTitolo() {
        return titolo;
    }

    public String getAutore() {
        return autore;
    }

    public int getNumCopie() {
        return numCopie;
    }

    public void incrementaCopie(int n) {
        if (n > 0) {
            numCopie += n;
        }
    }

    public boolean decrementaCopie(int n) {
        if (n <= numCopie && n > 0) {
            numCopie -= n;
            return true;
        }
        return false;
    }
}

