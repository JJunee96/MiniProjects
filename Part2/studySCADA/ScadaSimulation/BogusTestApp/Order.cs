using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BogusTestApp
{
    public class Order  // 주문 테이블
    {
        public Guid Id { get; set; } // 키값
        public DateTime Date { get; set; } // 주문일자
        public Decimal OrderValue { get; set; } // 주문갯수
        public bool Shipped { get; set; } // 선적여부
    }
}