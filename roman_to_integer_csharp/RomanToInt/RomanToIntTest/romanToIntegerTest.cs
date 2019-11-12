using NUnit.Framework;
using System.Linq;

namespace RomanToIntTest
{
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {

            var subject = new Solution();
            string[] testCase = { "III", "IV", "VI", "XXIV" };
            int[] expectedResult = { 3, 4, 6, 24 };
            int[] result = new int[4];

            for (int i = 0; i < testCase.Length; i++)
            {
                result[i] = subject.RomanToInt(testCase[i]);
            }

            Assert.That(result.SequenceEqual(expectedResult));
        }
    }
}