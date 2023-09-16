public class TiposJava {

    //Tipos primitivos: byte, short, int, long, float, double e char. Estes tipos de dados, quando declarados, são criados estaticamente somente podem mudar de tipo quando fazemos tecnicas de cast
    public static void main(String[] args) {
        String Nome = "Thiago";
        System.out.println(Conversora());
        System.out.println(Nome);
    }

    public static int Conversora(){
        // Este método nao deve ser implementado, mas apenas utilizado como entendimento do outro comentário
        /*
         *  Quando queremos converter um tipoo de dado para outro tipo de dado, nos fazemos na forma de cast, da seguinte forma
         */

        short dobro = 42;
        int inteiro = (int) dobro;
        return inteiro;
    }
}
