using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BogusTestApp
{
    public class Customer // 고객 테이블 매핑
    {
        public Guid Id { get; set; } // 고객 아이디
        public string Name { get; set; } // 고객 명
        public string Address { get; set; } // 고객주소
        public string Phone { get; set; } // 전화번호
        public string ContactName { get; set; } // 연락처명
        public IEnumerable<Order> Orders { get; set; } // 주문한 리스트
    }
}
