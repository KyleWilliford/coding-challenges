package c1;

import lombok.extern.slf4j.Slf4j;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

@Slf4j
public class Counterfeit {

    public static void main(String[] args) {
        List<String> serialNumbers = Arrays.asList("AVG190420T", "RTF20001000Z", "QWER201850G", "AFA199620E", "ERT1947200T", "RTY20202004", "DRV1984500Y", "TB2010400G");
        int sum = countCounterfeit(serialNumbers);
        logger.info("{}", sum);
    }

    // AVG190420T
    public static int countCounterfeit(List<String> serialNumber) {
        int sum = 0;
        Pattern p = Pattern.compile("^([A-Z]{3})(19\\d\\d|200\\d|201\\d)(10|20|50|100|200|500|1000)([A-Z])$");
        Set<String> distinctCheck;
        for (String s : serialNumber) {
            Matcher m = p.matcher(s);
            if (m.find()) {
                for (int i = 1; i < m.groupCount() + 1; i++) {
                    String group = m.group(i);
//                    logger.info(group);
                    if (i == 1) {
                        distinctCheck = new HashSet<>(Arrays.asList(group.split("")));
                        if (distinctCheck.size() != 3) {
                            break;
                        }
                    }
                    if (i == 3) {
//                        logger.info("Valid amount: {} sn {}", group, m.group(0));
                        sum += Integer.parseInt(group);
                    }
                }
            }
        }
        return sum;
    }
}
