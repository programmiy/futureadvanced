using System;

namespace AccessModifiersExample
{
    public class ExampleClass
    {
        // public 메서드: 모든 코드에서 접근 가능
        public void PublicMethod()
        {
            Console.WriteLine("Public method");
        }

        // private 메서드: 동일한 클래스 내에서만 접근 가능
        private void PrivateMethod()
        {
            Console.WriteLine("Private method");
        }

        // protected 메서드: 동일한 클래스 및 파생 클래스에서 접근 가능
        protected void ProtectedMethod()
        {
            Console.WriteLine("Protected method");
        }

        // internal 메서드: 동일한 어셈블리 내에서만 접근 가능
        internal void InternalMethod()
        {
            Console.WriteLine("Internal method");
        }

        // protected internal 메서드: 동일한 어셈블리 내 또는 파생 클래스에서 접근 가능
        protected internal void ProtectedInternalMethod()
        {
            Console.WriteLine("Protected internal method");
        }

        // private protected 메서드: 동일한 클래스 내 또는 동일한 어셈블리 내의 파생 클래스에서 접근 가능
        private protected void PrivateProtectedMethod()
        {
            Console.WriteLine("Private protected method");
        }

        // Main 메서드: 프로그램의 진입점
        static void Main(string[] args)
        {
            ExampleClass example = new ExampleClass();
            example.PublicMethod();
            example.InternalMethod();
            example.ProtectedInternalMethod();
            // example.PrivateMethod(); // 접근 불가
            // example.ProtectedMethod(); // 접근 불가
            // example.PrivateProtectedMethod(); // 접근 불가
        }
    }
}